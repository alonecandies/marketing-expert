# Marketing Expert

A full-stack AI-powered marketing assistant platform.

## Features

- AI-powered marketing expert (LangChain + OpenAI GPT-4 Turbo)
- User authentication (sign up, sign in, JWT, top-up credits)
- Persistent conversation memory (MongoDB)
- Marketing tasks: strategy, content generation, campaign analysis, branding, and more
- React frontend (shadcn/ui)
- Clean architecture backend (FastAPI, MySQL, MongoDB)
- Docker Compose orchestration

## Tech Stack

- **Backend:** FastAPI, LangChain, OpenAI GPT-4 Turbo, MySQL, MongoDB, SQLAlchemy, PyMongo, Docker
- **Frontend:** React, shadcn/ui, Tailwind CSS, Vite, Yarn, Docker

## Setup & Installation

### Prerequisites

- Docker & Docker Compose installed

### Quick Start

1. Clone the repository:
   ```sh
   git clone https://github.com/alonecandies/marketing-expert.git
   cd marketing-expert
   ```
2. Copy and configure environment variables as needed (see `.env.example` if present).
3. Build and start all services:
   ```sh
   docker compose build
   docker compose up
   ```
4. Access the app:
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API: [http://localhost:8000](http://localhost:8000)

## Folder Structure

```
marketing-expert/
├── backend/         # FastAPI backend
│   ├── app/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/        # React frontend
│   ├── src/
│   ├── package.json
│   ├── yarn.lock
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Usage

- Sign up, sign in, and top up credits on the frontend.
- Start a conversation with the AI marketing expert.
- Ask questions, request marketing plans, generate content, and more.
- View conversation history and manage your profile.

## Contributing

Pull requests and suggestions are welcome! Please open an issue to discuss changes.

## License

MIT
