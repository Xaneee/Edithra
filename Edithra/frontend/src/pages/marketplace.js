import { useState, useEffect } from 'react';
import { getMarketplaceItems } from '@/utils/payments';

export default function Marketplace() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        await fetchItems();
    }, []);

    const fetchItems = async () => {
        const data = await getMarketplaceItems();
        setItems(data);
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Marketplace</h1>
            {items.map((item) => (
                <div key={item.id} className='bg-gradient-to-r from-blue-800 to-gray-800 p-4 rounded-lg mt-2'>
                    <h2>{item.name} - ${item.price}</h2>
                    <button className='bg-gradient-to-r from-green-500 to-teal-500 hover:scale-105 transition transform duration-300 px-4 py-2 mt-2'>Buy</button>
                </div>
            ))}
        </div>
    );
}


import { useState, useEffect } from 'react';
import { getMarketplaceItems, purchaseItem } from '@/utils/payments';

export default function Marketplace() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        await fetchItems();
    }, []);

    const fetchItems = async () => {
        const data = await getMarketplaceItems();
        setItems(data);
    };

    const handlePurchase = async (itemId) => {
        await purchaseItem(itemId);
        alert('Purchase successful!');
    };

    return (
        <div className='min-h-screen bg-gradient-to-r from-blue-900 to-gray-900 text-gray-100 p-6'>
            <h1 className='text-2xl font-bold'>Marketplace</h1>
            {items.map((item) => (
                <div key={item.id} className='bg-gradient-to-r from-blue-800 to-gray-800 p-4 rounded-lg mt-2'>
                    <h2>{item.name} - ${item.price}</h2>
                    <button onClick={() => handlePurchase(item.id)} className='bg-gradient-to-r from-green-500 to-teal-500 hover:scale-105 transition transform duration-300 px-4 py-2 mt-2'>Buy</button>
                </div>
            ))}
        </div>
    );
}

