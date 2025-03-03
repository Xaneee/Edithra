import LiveNotifications from '@/components/LiveNotifications';

export default function LiveUpdates() {
    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Live Game Updates</h1>
            <LiveNotifications />
        </div>
    );
}


