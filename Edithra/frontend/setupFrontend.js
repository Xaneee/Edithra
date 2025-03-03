const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, 'gamesync-frontend');

const files = {
    "src/pages/index.js": "export default function Home() { return <h1>Welcome to GameSync AI</h1>; }",
    "src/pages/login.js": "export default function Login() { return <h1>Login Page</h1>; }",
    "src/pages/dashboard.js": "export default function Dashboard() { return <h1>Dashboard</h1>; }",
    "src/components/Profile.js": "export default function Profile({ user }) { return <div>User: {user?.name}</div>; }",
    "src/utils/api.js": "// API integration logic will go here",
    "src/utils/auth.js": "// Authentication helper functions"
};

// Create directories
Object.keys(files).forEach(filePath => {
    const fullPath = path.join(baseDir, filePath);
    fs.mkdirSync(path.dirname(fullPath), { recursive: true });
    fs.writeFileSync(fullPath, files[filePath]);
});

console.log("✅ GameSync AI Frontend Structure Created!");


