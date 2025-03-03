import { useState, useEffect } from 'react';

export default function LiveNotifications() {
    const [notifications, setNotifications] = useState([]);

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:5000');

        ws.onmessage = (event) => {
            setNotifications((prev) => [...prev, event.data]);
        };

        return () => ws.close();
    }, []);

    return (
        <div className='bg-gradient-to-r from-blue-800 to-gray-800 p-4 rounded-lg mt-4'>
            <h2 className='text-xl font-bold'>Live Notifications</h2>
            {notifications.length > 0 ? (
                notifications.map((note, index) => (
                    <p key={index}>{note}</p>
                ))
            ) : (
                <p>No live updates yet</p>
            )}
        </div>
    );
}


