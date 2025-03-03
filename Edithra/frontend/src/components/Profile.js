export default function Profile({ user }) {
    if (!user) return <p>Loading user...</p>;
    return (
        <div className='bg-gradient-to-r from-blue-800 to-gray-800 p-4 rounded-lg'>
            <h2 className='text-xl font-bold'>User Profile</h2>
            <p>Name: {user.name}</p>
            <p>Email: {user.email}</p>
        </div>
    );
}


