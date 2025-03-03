import { useState, useEffect } from 'react';
import { getCloudGPUStatus } from '@/utils/cloudGPU';

export default function CloudGPU() {
    const [status, setStatus] = useState(null);

    useEffect(() => {
        fetchStatus();
    }, []);

    const fetchStatus = async () => {
        const gpuStatus = await getCloudGPUStatus();
        setStatus(gpuStatus);
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Cloud GPU Status</h1>
            {status ? <p className='bg-gradient-to-r from-blue-800 to-gray-800 p-4 rounded-lg'>{status}</p> : <p>Checking GPU status...</p>}
        </div>
    );
}


