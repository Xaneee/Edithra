import { signInWithGoogle } from '@/utils/auth';

export default function Login() {
    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 flex flex-col justify-center items-center'>
            <h1 className='text-2xl font-bold'>Login</h1>
            <button onClick={signInWithGoogle} className='bg-gradient-to-r from-green-500 to-teal-500 hover:scale-105 transition transform duration-300 text-gray-100 px-4 py-2 mt-4'>Sign in with Google</button>
        </div>
    );
}


