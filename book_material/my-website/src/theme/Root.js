import React from 'react';
import ChatWidget from '../components/ChatWidget';

// Wrapper to inject Global components like the Chat Widget
export default function Root({ children }) {
    return (
        <>
            {children}
            <ChatWidget />
        </>
    );
}
