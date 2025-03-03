import { useState } from 'react';
import { uploadVideo } from '@/utils/cloudStorage';

export default function VideoProcessing() {
    const [file, setFile] = useState(null);

    const handleUpload = async () => {
        if (file) {
            const response = await uploadVideo(file);
            alert(response.message);
        }
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Video Upload</h1>
            <input type='file' onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleUpload} className='bg-gradient-to-r from-blue-500 to-green-500 hover:scale-105 transition transform duration-300 px-4 py-2 mt-4'>Upload</button>
        </div>
    );
}


