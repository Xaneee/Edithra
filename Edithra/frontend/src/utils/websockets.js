export const connectWebSocket = () => {
    const ws = new WebSocket('ws://localhost:5000');
    return ws;
};


