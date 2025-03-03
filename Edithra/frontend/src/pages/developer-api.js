import { useState, useEffect } from 'react';
import { getDeveloperAPI } from '@/utils/devAPI';

export default function DeveloperAPI() {
    const [apiData, setApiData] = useState(null);

    useEffect(() => {
        fetchAPIInfo();
    }, []);

    const fetchAPIInfo = async () => {
        const data = await getDeveloperAPI();
        setApiData(data);
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Developer API</h1>
            {apiData ? <pre className='bg-gradient-to-r from-blue-800 to-gray-800 p-4 rounded-lg'>{JSON.stringify(apiData, null, 2)}</pre> : <p>Loading API details...</p>}
        </div>
    );
}


