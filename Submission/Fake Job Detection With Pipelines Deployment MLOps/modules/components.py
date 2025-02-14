"""Initiate TFX pipeline components"""

import os
import tensorflow_model_analysis as tfma
from tfx.components import (
    CsvExampleGen,
    StatisticsGen,
    SchemaGen,
    ExampleValidator,
    Transform,
    Trainer,
    Tuner,
    Evaluator,
    Pusher,
)
from tfx.proto import example_gen_pb2, trainer_pb2, pusher_pb2
from tfx.types import Channel
from tfx.dsl.components.common.resolver import Resolver
from tfx.types.standard_artifacts import Model, ModelBlessing
from tfx.dsl.input_resolution.strategies.latest_blessed_model_strategy import LatestBlessedModelStrategy


def create_example_gen(data_dir):
    """Create the ExampleGen component."""
    output = example_gen_pb2.Output(
        split_config=example_gen_pb2.SplitConfig(splits=[
            example_gen_pb2.SplitConfig.Split(name="train", hash_buckets=8),
            example_gen_pb2.SplitConfig.Split(name="eval", hash_buckets=2),
        ])
    )
    return CsvExampleGen(input_base=data_dir, output_config=output)


def create_statistics_gen(example_gen):
    """Create the StatisticsGen component."""
    return StatisticsGen(examples=example_gen.outputs["examples"])


def create_schema_gen(statistics_gen):
    """Create the SchemaGen component."""
    return SchemaGen(statistics=statistics_gen.outputs["statistics"])


def create_example_validator(statistics_gen, schema_gen):
    """Create the ExampleValidator component."""
    return ExampleValidator(
        statistics=statistics_gen.outputs['statistics'],
        schema=schema_gen.outputs['schema']
    )


def create_transform(example_gen, schema_gen, transform_module):
    """Create the Transform component."""
    return Transform(
        examples=example_gen.outputs['examples'],
        schema=schema_gen.outputs['schema'],
        module_file=os.path.abspath(transform_module),
    )


def create_trainer(transform, schema_gen, training_module, training_steps, eval_steps):
    """Create the Trainer component."""
    return Trainer(
        module_file=os.path.abspath(training_module),
        examples=transform.outputs['transformed_examples'],
        transform_graph=transform.outputs['transform_graph'],
        schema=schema_gen.outputs['schema'],
        train_args=trainer_pb2.TrainArgs(splits=['train'], num_steps=training_steps),
        eval_args=trainer_pb2.EvalArgs(splits=['eval'], num_steps=eval_steps),
    )


def create_tuner(transform, schema_gen, tuner_module):
    """Create the Tuner component."""
    return Tuner(
        module_file=os.path.abspath(tuner_module),
        examples=transform.outputs['transformed_examples'],
        transform_graph=transform.outputs['transform_graph'],
        schema=schema_gen.outputs['schema'],
        train_args=trainer_pb2.TrainArgs(splits=['train']),
        eval_args=trainer_pb2.EvalArgs(splits=['eval']),
    )


def create_model_resolver():
    """Create the model resolver."""
    return Resolver(
        strategy_class=LatestBlessedModelStrategy,
        model=Channel(type=Model),
        model_blessing=Channel(type=ModelBlessing),
    ).with_id('Latest_blessed_model_resolver')


def create_evaluator(example_gen, trainer, model_resolver):
    """Create the Evaluator component."""
    slicing_specs = [
        tfma.SlicingSpec(),
        tfma.SlicingSpec(feature_keys=["is_fake"]),
    ]
    metrics_specs = [
        tfma.MetricsSpec(metrics=[
            tfma.MetricConfig(class_name='AUC'),
            tfma.MetricConfig(class_name="Precision"),
            tfma.MetricConfig(class_name="Recall"),
            tfma.MetricConfig(class_name="ExampleCount"),
            tfma.MetricConfig(class_name='BinaryAccuracy', threshold=tfma.MetricThreshold(
                value_threshold=tfma.GenericValueThreshold(lower_bound={'value': 0.5}),
                change_threshold=tfma.GenericChangeThreshold(direction=tfma.MetricDirection.HIGHER_IS_BETTER,
                                                             absolute={'value': 0.0001}),
            )),
        ])
    ]
    eval_config = tfma.EvalConfig(
        model_specs=[tfma.ModelSpec(label_key='is_fake')],
        slicing_specs=slicing_specs,
        metrics_specs=metrics_specs,
    )
    return Evaluator(
        examples=example_gen.outputs['examples'],
        model=trainer.outputs['model'],
        baseline_model=model_resolver.outputs['model'],
        eval_config=eval_config,
    )


def create_pusher(trainer, evaluator, serving_model_dir):
    """Create the Pusher component."""
    return Pusher(
        model=trainer.outputs["model"],
        model_blessing=evaluator.outputs["blessing"],
        push_destination=pusher_pb2.PushDestination(
            filesystem=pusher_pb2.PushDestination.Filesystem(base_directory=serving_model_dir)
        ),
    )


def init_components(
    data_dir,
    transform_module,
    training_module,
    training_steps,
    tuner_module,
    eval_steps,
    serving_model_dir,
):
    """Initialize TFX pipeline components.

    Args:
        data_dir (str): A path to the data.
        transform_module (str): A path to the transform module.
        training_module (str): A path to the training module.
        training_steps (int): Number of training steps.
        eval_steps (int): Number of evaluation steps.
        serving_model_dir (str): A path to the serving model directory.

    Returns:
        components (tuple): Tuple of TFX components.
    """

    # Create components
    example_gen = create_example_gen(data_dir)
    statistics_gen = create_statistics_gen(example_gen)
    schema_gen = create_schema_gen(statistics_gen)
    example_validator = create_example_validator(statistics_gen, schema_gen)
    transform = create_transform(example_gen, schema_gen, transform_module)
    trainer = create_trainer(transform, schema_gen, training_module, training_steps, eval_steps)
    tuner = create_tuner(transform, schema_gen, tuner_module)
    model_resolver = create_model_resolver()
    evaluator = create_evaluator(example_gen, trainer, model_resolver)
    pusher = create_pusher(trainer, evaluator, serving_model_dir)

    components = (
        example_gen,
        statistics_gen,
        schema_gen,
        example_validator,
        transform,
        trainer,
        tuner,
        model_resolver,
        evaluator,
        pusher,
    )

    return components
