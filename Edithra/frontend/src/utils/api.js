export const getUserStats = async (email) => {
    if (!email) return null;
    return {
        gamesPlayed: 120,
        winRate: 58,
        rank: 'Diamond'
    };
};


export const getAIHighlights = async () => {
    return [
        { title: 'Epic Clutch', videoUrl: '/videos/highlight1.mp4' },
        { title: 'Insane Headshot', videoUrl: '/videos/highlight2.mp4' }
    ];
};


