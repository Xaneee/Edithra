import { useState, useEffect } from 'react';
import { getLeaderboard } from '@/utils/leaderboard';

export default function Leaderboard() {
    const [players, setPlayers] = useState([]);

    useEffect(() => {
        fetchLeaderboard();
    }, []);

    const fetchLeaderboard = async () => {
        const data = await getLeaderboard();
        setPlayers(data);
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Leaderboard</h1>
            <ul>
                {players.map((player, index) => (
                    <li key={index} className='mt-2'>{index + 1}. {player.name} - {player.rank}</li>
                ))}
            </ul>
        </div>
    );
}


