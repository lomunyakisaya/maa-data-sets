---
library_name: peft
license: cc-by-nc-4.0
base_model: facebook/nllb-200-distilled-600M
tags:
- base_model:adapter:facebook/nllb-200-distilled-600M
- lora
- transformers
model-index:
- name: English-to-Maasai-language-translation-LoRA
  results: []
datasets:
- KnoxDevelopers/english_maasai_pair_sentences
language:
- en
- mas
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English-to-Maasai-language-translation-LoRA

This model is a fine-tuned version of [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) on the [English-Maasai](https://huggingface.co/datasets/KnoxDevelopers/english_maasai_pair_sentences) dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3882

## Model description

A LoRA adapter for translating text from English to Maasai.

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 7.3063        | 1.0   | 1744  | 3.3755          |
| 6.4322        | 2.0   | 3488  | 2.9127          |
| 5.8681        | 3.0   | 5232  | 2.6750          |
| 5.4832        | 4.0   | 6976  | 2.5355          |
| 5.3153        | 5.0   | 8720  | 2.4531          |
| 5.2278        | 6.0   | 10464 | 2.4057          |
| 5.2409        | 7.0   | 12208 | 2.3882          |

### Evaluation metrics
| Metric        | Results | Explained
|:-------------:|:-------:|:-------------:
| sacrebleu     | 7.230   | Evaluation matches exact word sequence referencing our ground truth and adapter output. 
|               |         | 0-20= translation is literal or broken, 20-50=good, >60=very good or identical training and test data.
| chrF++        | 36.480  | Eval matches character sequence instead of whole words.
|               |         | Model adapter is getting the root words and grammar concepts right but using different word variations or spellings than our ground truth, this is concluded due to the low sacrebleu results.

### Framework versions

- PEFT 0.19.1
- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2