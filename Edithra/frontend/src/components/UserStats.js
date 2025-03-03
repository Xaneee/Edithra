export default function UserStats({ stats }) {
    return (
        <div className='bg-gradient-to-r from-blue-800 to-gray-800 p-4 rounded-lg mt-4'>
            <h2 className='text-xl font-bold'>User Stats</h2>
            {stats ? (
                <ul>
                    <li>Games Played: {stats.gamesPlayed}</li>
                    <li>Win Rate: {stats.winRate}%</li>
                    <li>Rank: {stats.rank}</li>
                </ul>
            ) : (
                <p>Loading stats...</p>
            )}
        </div>
    );
}


