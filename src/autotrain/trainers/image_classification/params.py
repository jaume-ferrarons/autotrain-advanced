from typing import Optional

from pydantic import Field

from autotrain.trainers.common import AutoTrainParams


class ImageClassificationParams(AutoTrainParams):
    """
    ImageClassificationParams is a configuration class for image classification training parameters.

    Attributes:
        data_path (str): Path to the dataset.
        model (str): Pre-trained model name or path. Default is "google/vit-base-patch16-224".
        username (Optional[str]): Hugging Face account username.
        lr (float): Learning rate for the optimizer. Default is 5e-5.
        epochs (int): Number of epochs for training. Default is 3.
        batch_size (int): Batch size for training. Default is 8.
        warmup_ratio (float): Warmup ratio for learning rate scheduler. Default is 0.1.
        gradient_accumulation (int): Number of gradient accumulation steps. Default is 1.
        optimizer (str): Optimizer type. Default is "adamw_torch".
        scheduler (str): Learning rate scheduler type. Default is "linear".
        weight_decay (float): Weight decay for the optimizer. Default is 0.0.
        max_grad_norm (float): Maximum gradient norm for clipping. Default is 1.0.
        seed (int): Random seed for reproducibility. Default is 42.
        train_split (str): Name of the training data split. Default is "train".
        valid_split (Optional[str]): Name of the validation data split.
        logging_steps (int): Number of steps between logging. Default is -1.
        project_name (str): Name of the project for output directory. Default is "project-name".
        auto_find_batch_size (bool): Automatically find optimal batch size. Default is False.
        mixed_precision (Optional[str]): Mixed precision training mode (fp16, bf16, or None).
        save_total_limit (int): Maximum number of checkpoints to keep. Default is 1.
        token (Optional[str]): Hugging Face Hub token for authentication.
        push_to_hub (bool): Whether to push the model to Hugging Face Hub. Default is False.
        eval_strategy (str): Evaluation strategy during training. Default is "epoch".
        image_column (str): Column name for images in the dataset. Default is "image".
        target_column (str): Column name for target labels in the dataset. Default is "target".
        log (str): Logging method for experiment tracking. Default is "none".
        early_stopping_patience (int): Number of epochs with no improvement for early stopping. Default is 5.
        early_stopping_threshold (float): Threshold for early stopping. Default is 0.01.
    """

    data_path: str = Field(None, title="Path to the dataset")
    model: str = Field("google/vit-base-patch16-224", title="Pre-trained model name or path")
    username: Optional[str] = Field(None, title="Hugging Face account username")
    lr: float = Field(5e-5, title="Learning rate for the optimizer")
    epochs: int = Field(3, title="Number of epochs for training")
    batch_size: int = Field(8, title="Batch size for training")
    warmup_ratio: float = Field(0.1, title="Warmup ratio for learning rate scheduler")
    gradient_accumulation: int = Field(1, title="Number of gradient accumulation steps")
    optimizer: str = Field("adamw_torch", title="Optimizer type")
    scheduler: str = Field("linear", title="Learning rate scheduler type")
    weight_decay: float = Field(0.0, title="Weight decay for the optimizer")
    max_grad_norm: float = Field(1.0, title="Maximum gradient norm for clipping")
    seed: int = Field(42, title="Random seed for reproducibility")
    train_split: str = Field("train", title="Name of the training data split")
    valid_split: Optional[str] = Field(None, title="Name of the validation data split")
    logging_steps: int = Field(-1, title="Number of steps between logging")
    project_name: str = Field("project-name", title="Name of the project for output directory")
    auto_find_batch_size: bool = Field(False, title="Automatically find optimal batch size")
    mixed_precision: Optional[str] = Field(None, title="Mixed precision training mode (fp16, bf16, or None)")
    save_total_limit: int = Field(1, title="Maximum number of checkpoints to keep")
    token: Optional[str] = Field(None, title="Hugging Face Hub token for authentication")
    push_to_hub: bool = Field(False, title="Whether to push the model to Hugging Face Hub")
    eval_strategy: str = Field("epoch", title="Evaluation strategy during training")
    image_column: str = Field("image", title="Column name for images in the dataset")
    target_column: str = Field("target", title="Column name for target labels in the dataset")
    log: str = Field("none", title="Logging method for experiment tracking")
    early_stopping_patience: int = Field(5, title="Number of epochs with no improvement for early stopping")
    early_stopping_threshold: float = Field(0.01, title="Threshold for early stopping")
