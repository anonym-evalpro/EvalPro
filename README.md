<h1 align="center">Enhancing AI4SE Benchmarking: A Survey, Search Aid, and Framework for Improved Evaluation</h1>

## Table of Contents

- [Introduction](#introduction)
- [Review](#review)
- [EvalProSearch](#EvalProSearch)
- [HumanEvalPro](#HumanEvalPro)

## Introduction

The growing use of artificial intelligence (AI) in software engineering (AI4SE) has highlighted the critical need for robust and consistent benchmarking practices. Many of the current benchmarks lack the rigor and standardization needed for precise model evaluation, limiting their effectiveness. Additionally, there is a shortage of comprehensive reviews that could help users navigate and understand existing benchmarks.

To address this challenge, we conducted an extensive survey of 111 AI4SE benchmarks, extracting insights and identifying key limitations in the existing evaluation methods. These findings informed the development of EvalProSearch, a novel tool designed to assist users in discovering relevant benchmarks and accessing associated literature. In a user study involving 20 practitioners and researchers, EvalProSearch was validated for its effectiveness and ease of use.

In addition, we created EvalPro, a framework aimed at enhancing benchmark quality. As a case study, we applied EvalPro to the widely-used HumanEval code generation benchmark to address its weaknesses. HumanEvalPro, the improved version, includes corrected errors, improved language conversions, increased test coverage, and heightened difficulty.

Our evaluation of ten state-of-the-art code language models on both HumanEval and HumanEvalPro showed a significant 31.22% average reduction in pass@1 scores, illustrating the challenges imposed by more rigorous benchmarks. This result emphasizes the importance of high-quality benchmarks for the development of more robust AI models in software engineering.

The EvalPro Suite, which includes the survey, tools, and improved benchmarks, is released as an open resource to drive future research in AI4SE and enhance benchmark standards.

## Review

The review section can be found [here](./Review/README.md).


## EvalProSearch

EvalProSearch is a tool that helps users discover relevant benchmarks and access associated literature. The tool can be found [here](https://evalpro.online/search.html).
The results of the user study on EvalProSearch can be found [here](./Search/README.md).


## HumanEvalPro

HumanEvalPro is an improved version of the HumanEval code generation benchmark.
The improvements made are based on the framework EvalPro. This framework is aimed at enhancing benchmark quality through a rigorous improvement process along with peer reviews.
An overview of the approach along with the specific applicability to HumanEval has been illustrated below.

![HumanEvalPro Improvement Process](./images/HumanEvalPro_approach.png)

The evaluation results of benchmark can be found [here](https://evalpro.online/leaderboard.html).
A more detailed description of HumanEvalPro can be found [here](./HumanEvalPro/README.md).