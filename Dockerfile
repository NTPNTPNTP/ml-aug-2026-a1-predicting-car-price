FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

# Install dependencies first (better layer caching)
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --frozen --no-dev

# Copy only what's needed to run the app (data/ and experiments.ipynb are excluded — not needed at runtime)
COPY app ./app
COPY model ./model

# main.py loads the model via a relative path ("../model/..."), so cwd must be app/
WORKDIR /code/app

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]