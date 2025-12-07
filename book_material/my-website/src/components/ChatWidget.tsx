import React, { useState } from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

// Configure Backend URL (Make configurable in real app)
const API_URL = "http://localhost:8001/api/v1";

// Simple ID generator for demo purposes
const getUserId = () => {
    let id = localStorage.getItem('chat_user_id');
    if (!id) {
        id = 'user_' + Math.random().toString(36).substr(2, 9);
        localStorage.setItem('chat_user_id', id);
    }
    return id;
};

export default function ChatWidget() {
    const [isOpen, setIsOpen] = useState(false);
    const [view, setView] = useState<'chat' | 'settings'>('chat');
    const [messages, setMessages] = useState([
        { role: 'assistant', content: 'Hi! I am your AI Teaching Assistant. Ask me anything about the book!' }
    ]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);

    // Profile State
    const [userId] = useState(getUserId());
    const [expertise, setExpertise] = useState('Beginner');
    const [hardware, setHardware] = useState('SimOnly');

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMsg = { role: 'user', content: input };
        setMessages([...messages, userMsg]);
        setLoading(true);
        setInput('');

        try {
            const response = await fetch(`${API_URL}/chat/rag`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    query: userMsg.content,
                    user_id: userId, // Pass user ID for personalization
                    history: []
                })
            });

            const data = await response.json();
            setMessages(prev => [...prev, { role: 'assistant', content: data.answer }]);
        } catch (e) {
            setMessages(prev => [...prev, { role: 'assistant', content: 'Error connecting to AI brain. Is the backend running?' }]);
        } finally {
            setLoading(false);
        }
    };

    const saveProfile = async () => {
        try {
            await fetch(`${API_URL}/profile`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    user_id: userId,
                    email: `${userId}@example.com`, // Placeholder
                    python_expertise: expertise,
                    hardware_access: hardware
                })
            });
            setView('chat');
            setMessages(prev => [...prev, { role: 'assistant', content: `Profile updated! I'll now tailor answers for a ${expertise} using ${hardware}.` }]);
        } catch (e) {
            console.error(e);
        }
    };

    return (
        <div className="chat-widget-container" style={{ position: 'fixed', bottom: 20, right: 20, zIndex: 9999 }}>
            {!isOpen && (
                <button
                    onClick={() => setIsOpen(true)}
                    style={{ width: 60, height: 60, borderRadius: 30, backgroundColor: '#25c2a0', border: 'none', color: 'white', cursor: 'pointer', fontSize: 24, boxShadow: '0 4px 10px rgba(0,0,0,0.2)' }}
                >
                    🤖
                </button>
            )}

            {isOpen && (
                <div style={{ width: 350, height: 500, backgroundColor: 'var(--ifm-background-surface-color)', borderRadius: 12, boxShadow: '0 5px 20px rgba(0,0,0,0.3)', display: 'flex', flexDirection: 'column', overflow: 'hidden', border: '1px solid var(--ifm-color-emphasis-200)' }}>

                    {/* Header */}
                    <div style={{ padding: 15, backgroundColor: '#25c2a0', color: 'white', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ fontWeight: 'bold' }}>AI Assistant</span>
                        <div>
                            <button onClick={() => setView(view === 'chat' ? 'settings' : 'chat')} style={{ background: 'none', border: 'none', color: 'white', cursor: 'pointer', marginRight: 10 }}>⚙️</button>
                            <button onClick={() => setIsOpen(false)} style={{ background: 'none', border: 'none', color: 'white', cursor: 'pointer', fontSize: 18 }}>×</button>
                        </div>
                    </div>

                    {/* Chat View */}
                    {view === 'chat' && (
                        <>
                            <div style={{ flex: 1, padding: 15, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 10 }}>
                                {messages.map((m, i) => (
                                    <div key={i} style={{
                                        alignSelf: m.role === 'user' ? 'flex-end' : 'flex-start',
                                        backgroundColor: m.role === 'user' ? '#e6f7ff' : '#f0f0f0',
                                        color: 'black',
                                        padding: '8px 12px',
                                        borderRadius: 12,
                                        maxWidth: '85%'
                                    }}>
                                        {m.content}
                                    </div>
                                ))}
                                {loading && <div style={{ color: 'gray', fontStyle: 'italic' }}>Thinking...</div>}
                            </div>
                            <div style={{ padding: 10, borderTop: '1px solid #ddd', display: 'flex', gap: 5 }}>
                                <input
                                    value={input}
                                    onChange={(e) => setInput(e.target.value)}
                                    onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
                                    placeholder="Ask a question..."
                                    style={{ flex: 1, padding: 8, borderRadius: 6, border: '1px solid #ccc' }}
                                />
                                <button onClick={sendMessage} style={{ backgroundColor: '#25c2a0', color: 'white', border: 'none', padding: '8px 12px', borderRadius: 6, cursor: 'pointer' }}>Send</button>
                            </div>
                        </>
                    )}

                    {/* Settings View */}
                    {view === 'settings' && (
                        <div style={{ padding: 20, color: 'var(--ifm-color-content)' }}>
                            <h3>Personalization</h3>
                            <p style={{ fontSize: '0.9em', color: 'gray' }}>Taylor the AI to your hardware.</p>

                            <label style={{ display: 'block', marginTop: 15, fontWeight: 'bold' }}>Python Level</label>
                            <select
                                value={expertise}
                                onChange={(e) => setExpertise(e.target.value)}
                                style={{ width: '100%', padding: 8, marginTop: 5, borderRadius: 4, border: '1px solid #ccc' }}
                            >
                                <option value="Beginner">Beginner</option>
                                <option value="Intermediate">Intermediate</option>
                                <option value="Advanced">Advanced</option>
                            </select>

                            <label style={{ display: 'block', marginTop: 15, fontWeight: 'bold' }}>Hardware Access</label>
                            <select
                                value={hardware}
                                onChange={(e) => setHardware(e.target.value)}
                                style={{ width: '100%', padding: 8, marginTop: 5, borderRadius: 4, border: '1px solid #ccc' }}
                            >
                                <option value="SimOnly">Simulation Only</option>
                                <option value="JetsonNano">Jetson Nano</option>
                                <option value="JetsonOrin">Jetson Orin</option>
                                <option value="RTX">RTX GPU Desktop</option>
                            </select>

                            <button
                                onClick={saveProfile}
                                style={{ width: '100%', marginTop: 20, padding: 10, backgroundColor: '#25c2a0', color: 'white', border: 'none', borderRadius: 6, cursor: 'pointer', fontWeight: 'bold' }}
                            >
                                Save Preferences
                            </button>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}
