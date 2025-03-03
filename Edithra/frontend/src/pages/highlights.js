import { useState, useEffect } from 'react';
import { getAIHighlights } from '@/utils/api';
import HighlightsList from '@/components/HighlightsList';

export default function Highlights() {
    const [highlights, setHighlights] = useState([]);

    useEffect(() => {
        fetchHighlights();
    }, []);

    const fetchHighlights = async () => {
        const data = await getAIHighlights();
        setHighlights(data);
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>AI Highlights</h1>
            <HighlightsList highlights={highlights} />
        </div>
    );
}


