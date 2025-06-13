#!/bin/bash

# AI Code Review Assistant - Docker Development Script

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_banner() {
    echo -e "${BLUE}"
    echo "================================================"
    echo "     AI Code Review Assistant - Docker"
    echo "================================================"
    echo -e "${NC}"
}

print_usage() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  up        Start all services"
    echo "  down      Stop all services"
    echo "  restart   Restart all services"
    echo "  logs      Show logs from all services"
    echo "  status    Show status of all services"
    echo "  clean     Remove all containers and volumes"
    echo "  build     Rebuild all images"
    echo "  shell     Open shell in backend container"
    echo ""
}

check_docker() {
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}Error: Docker is not installed${NC}"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        echo -e "${RED}Error: Docker Compose is not installed${NC}"
        exit 1
    fi
}

start_services() {
    echo -e "${YELLOW}🐳 Starting AI Code Review Assistant services...${NC}"
    echo -e "${BLUE}This may take a few minutes on first run...${NC}"
    
    docker-compose up -d --build
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Services started successfully!${NC}"
        echo ""
        echo -e "${YELLOW}📊 Service URLs:${NC}"
        echo "  🌐 Frontend:  http://localhost:3000"
        echo "  🚀 Backend:   http://localhost:8000"
        echo "  📖 API Docs: http://localhost:8000/docs"
        echo "  🐘 PostgreSQL: localhost:5432"
        echo "  🍃 MongoDB: localhost:27017"
        echo "  🔴 Redis: localhost:6379"
        echo ""
        echo -e "${BLUE}💡 To view logs: ./scripts/docker-dev.sh logs${NC}"
        echo -e "${BLUE}💡 To stop: ./scripts/docker-dev.sh down${NC}"
    else
        echo -e "${RED}❌ Failed to start services${NC}"
        exit 1
    fi
}

stop_services() {
    echo -e "${YELLOW}🛑 Stopping all services...${NC}"
    docker-compose down
    echo -e "${GREEN}✅ Services stopped${NC}"
}

restart_services() {
    echo -e "${YELLOW}🔄 Restarting all services...${NC}"
    docker-compose restart
    echo -e "${GREEN}✅ Services restarted${NC}"
}

show_logs() {
    echo -e "${YELLOW}📋 Showing logs from all services...${NC}"
    echo -e "${BLUE}Press Ctrl+C to exit logs${NC}"
    docker-compose logs -f
}

show_status() {
    echo -e "${YELLOW}📊 Service Status:${NC}"
    docker-compose ps
    echo ""
    echo -e "${YELLOW}🔍 Container Health:${NC}"
    docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
}

clean_all() {
    echo -e "${RED}🧹 This will remove ALL containers, volumes, and images${NC}"
    echo -e "${YELLOW}Are you sure? (y/N): ${NC}"
    read -r response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        echo -e "${YELLOW}Cleaning up...${NC}"
        docker-compose down -v --remove-orphans
        docker system prune -af --volumes
        echo -e "${GREEN}✅ Cleanup complete${NC}"
    else
        echo -e "${BLUE}Cleanup cancelled${NC}"
    fi
}

build_images() {
    echo -e "${YELLOW}🔨 Rebuilding all images...${NC}"
    docker-compose build --no-cache
    echo -e "${GREEN}✅ Images rebuilt${NC}"
}

open_shell() {
    echo -e "${YELLOW}🐚 Opening shell in backend container...${NC}"
    docker-compose exec backend bash
}

# Main script
print_banner
check_docker

case "${1:-}" in
    up)
        start_services
        ;;
    down)
        stop_services
        ;;
    restart)
        restart_services
        ;;
    logs)
        show_logs
        ;;
    status)
        show_status
        ;;
    clean)
        clean_all
        ;;
    build)
        build_images
        ;;
    shell)
        open_shell
        ;;
    "")
        echo -e "${YELLOW}No command specified${NC}"
        print_usage
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        print_usage
        exit 1
        ;;
esac

