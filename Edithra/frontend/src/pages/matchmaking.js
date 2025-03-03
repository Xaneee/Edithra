import { useState } from 'react';

export default function Matchmaking() {
    const [match, setMatch] = useState(null);

    const findMatch = async () => {
        setMatch('You have been matched with PlayerX!');
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Matchmaking</h1>
            <button onClick={findMatch} className='bg-gradient-to-r from-blue-500 to-green-500 hover:scale-105 transition transform duration-300 px-4 py-2 mt-4'>Find Match</button>
            {match && <p className='mt-4'>{match}</p>}
        </div>
    );
}
import { useState } from 'react';
import { findMatch } from '@/utils/matchmaking';

export default function Matchmaking() {
    const [match, setMatch] = useState(null);

    const handleFindMatch = async () => {
        const matchedPlayer = await findMatch();
        setMatch(matchedPlayer);
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Matchmaking</h1>
            <button onClick={handleFindMatch} className='bg-gradient-to-r from-blue-500 to-green-500 hover:scale-105 transition transform duration-300 px-4 py-2 mt-4'>Find Match</button>
            {match && <p className='mt-4'>Matched with: {match.name}</p>}
        </div>
    );
}


