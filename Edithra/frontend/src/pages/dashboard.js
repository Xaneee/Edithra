import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { signOut } from '@/utils/auth';
import { getUserStats } from '@/utils/api';
import Profile from '@/components/Profile';
import UserStats from '@/components/UserStats';
import { useAuthContext } from '@/components/AuthProvider';

export default function Dashboard() {
    const { user } = useAuthContext();
    const router = useRouter();
    const [stats, setStats] = useState(null);

    useEffect(() => {
        if (!user) {
            router.push('/login');
            return;
        }
        fetchStats();
    }, [user]);

    const fetchStats = async () => {
        if (user?.email) {
            const userStats = await getUserStats(user.email);
            setStats(userStats);
        }
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>GameSync AI Dashboard</h1>
            {user && <Profile user={user} />}
            <UserStats stats={stats} />
            <button onClick={signOut} className='bg-gradient-to-r from-red-500 to-orange-500 hover:scale-105 transition transform duration-300 px-4 py-2 mt-4'>Logout</button>
        </div>
    );
}


