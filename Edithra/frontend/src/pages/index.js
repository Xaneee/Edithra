export default function Home() {
    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-3xl font-bold'>Welcome to GameSync AI</h1>
            <a href='/dashboard'><button className='bg-gradient-to-r from-blue-500 to-green-500 hover:scale-105 transition transform duration-300 text-gray-100 px-4 py-2 mt-4'>Go to Dashboard</button></a>
        </div>
    );
}


