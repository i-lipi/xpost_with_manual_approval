# Xpost with manual approval Flow

I built an AI-powered pipeline that generates humorous, Shakespearean-style X posts based on input topics using CrewAI and OpenAI. The system includes a self-evaluation loop where a second agent validates the generated post for tone, length, and quality before approval. Approved posts are then automatically published to X using Tweepy, with all steps tracked via an Excel interface and logging system.

## Overview

This flow automates the generation and approval of X (Twitter) posts through the following steps:

1. **Generate Initial Output**: The `ShakespeareanXPostCrew` generates an initial Shakespearean-style post (X post) on a given topic, such as "Flying cars". This post is crafted to be humorous and playful, adhering to specific character limits and style guidelines.

2. **Evaluate Output**: The `XPostReviewCrew` evaluates the generated post to ensure it meets the required criteria, such as character count, tone, no fluff and absence of emojis. The crew provides feedback on the post's validity and quality.

3. **Human/Agent Approval**: Once the generated output is populated in the excel sheet, we manually check if the content satisfies our requirements.A man-in-the-middle system approves, rejects, or holds the post for review, using an Excel-based interface.

4. **Iterate with Feedback**: If the post does not meet the criteria, the flow iterates by regenerating the post with the feedback provided. This iterative process continues until the post is valid or a maximum retry limit is reached.

5. **Post to Twitter and Track status**: Once approved, the tweet is published using the X API [[https://developer.x.com]. All data is logged and updated in a centralized Excel sheet for traceability.

This pattern of automatic self-evaluation is crucial for developing robust AI systems that can adapt and improve over time, ensuring high-quality outputs through iterative refinement.

## Self-Evaluation Loop Pattern

This project demonstrates **self-evaluation with agent feedback**, making it ideal for:

- AI-generated content pipelines
- Internal review loops for social teams
- Use cases requiring **quality assurance before publishing**

## Customizing

This project serves as a blueprint for building intelligent, approval-driven social media automation pipelines.

While the current implementation focuses on generating humorous, Shakespearean-style X posts, the entire flow is fully customizable and can be adapted for various real-world use cases, including:

-Enterprise announcements (e.g., product launches, company updates)
-Project showcases with AI-generated summaries
-Targeted brand engagement campaigns with specific tone/style
-Internal team updates or automated HR posts
-Event-based or scheduled content pipelines

By modifying the agent prompts, tone, review criteria, or output format, this framework can scale into a robust enterprise-level content automation system with full control over quality and brand voice.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:
    
```bash
crewai flow kickoff 
```


This command initializes the self-evaluation loop flow, assembling the agents and assigning them tasks as defined in your configuration.

The unmodified example will generate a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Flow

The self-evaluation loop flow is composed of 2 Crews. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your flow.

This flow is centered around two major Crews: the `ShakespeareanXPostCrew` and the `XPostReviewCrew`. The `ShakespeareanXPostCrew` is responsible for generating a Shakespearean-style post (X post) on a given topic, while the `XPostReviewCrew` evaluates the generated post to ensure it meets specific criteria. The process is iterative, using feedback from the review to refine the post until it is valid or a maximum retry limit is reached.

### Flow Structure

1. **Generate Initial Output**: A Crew generates the initial output based on predefined criteria.

2. **Evaluate Output**: Another Crew evaluates the output, providing feedback on its validity and quality.

3. **Iterate with Feedback**: If necessary, the initial Crew is re-run with feedback to improve the output.

4. **Finalize and Save**: Once validated, the output is saved for further use.

By understanding the flow structure, you can see how multiple Crews are orchestrated to work together, each handling a specific part of the self-evaluation process. This modular approach allows for efficient and scalable automation.

## Support

For support, questions, or feedback regarding the Self Evaluation Loop Flow or crewAI:

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
