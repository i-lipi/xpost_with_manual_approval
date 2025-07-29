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

