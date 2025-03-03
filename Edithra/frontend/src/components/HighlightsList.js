export default function HighlightsList({ highlights }) {
    return (
        <div className='mt-4'>
            {highlights.length > 0 ? (
                highlights.map((highlight, index) => (
                    <div key={index} className='bg-gradient-to-r from-blue-800 to-gray-800 p-4 rounded-lg mt-2'>
                        <h2 className='text-lg font-bold'>{highlight.title}</h2>
                        <video src={highlight.videoUrl} controls className='w-full mt-2'></video>
                    </div>
                ))
            ) : (
                <p>No highlights available</p>
            )}
        </div>
    );
}


