export const getMarketplaceItems = async () => {
    return [
        { id: 1, name: 'Game Skin', price: 5.99 },
        { id: 2, name: 'Weapon Upgrade', price: 9.99 }
    ];
};

export const purchaseItem = async (itemId) => {
    console.log('Purchasing item ID:', itemId);
    return { message: 'Purchase successful!' };
};


