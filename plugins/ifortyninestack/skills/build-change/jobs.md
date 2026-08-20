# Background jobs and external APIs

- Pass IDs and simple scalar values to the job.
- Reload records inside the worker.
- Make every side effect safe to retry.
- Raise or classify missing records according to the intended retry behavior.
- Do not enqueue inside a database transaction unless the transaction boundary is intentional and documented.
- Prefer enqueueing after commit.
- If required enqueueing fails, update the domain status to an explicit failure state and return an appropriate request error.
- Set external API timeouts.
- Define retryable and terminal errors.
- Keep partial failure from creating contradictory persisted state.
- Chunk, batch, or fan out work that is too large for one reliable job.
- Keep notifications best effort after the primary write succeeds.
- Make job status, trace IDs, and failure messages useful during an incident.
- Centralize LLM provider retention controls and send request-level no-store options when supported.
