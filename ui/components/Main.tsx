"use client";

import React, { useState, useEffect } from 'react';
import { postFastAPIText } from '@/utils/fastApiCall';
import { v4 as uuidv4 } from 'uuid';


export default function Main() {
    const [podcastName, setPodcastName] = useState('');
    const [episodeName, setEpisodeName] = useState('');
    const [summary, setSummary] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [clientId, setClientId] = useState<string>("");

    const generateClientId = () => {
        const generatedId = uuidv4(); //UUID
        setClientId(generatedId);
        return generatedId;
    };

    useEffect(() => {
        const storedClientId = localStorage.getItem("clientId");

        if (storedClientId) {
            setClientId(storedClientId);
        } else {
            const newClientId = generateClientId();
            localStorage.setItem("clientId", newClientId);
        }
    }, []);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        if (!podcastName.trim() || !episodeName.trim()) {
            alert('Both fields are required.');
            return;
        }

        setIsLoading(true);
        setSummary('');
        try {
            const response = await postFastAPIText('summarize', podcastName, episodeName, clientId);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            setSummary(data.text); 
        } catch (error) {
            console.error('Error fetching summary:', error);
            alert('Failed to fetch summary.');
        } finally {
            setIsLoading(false);
        }
    }

    return (
        <div
            id="main" 
            className="flex flex-col justify-center items-center w-full h-fit bg-gray-200 dark:bg-gray-700">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={podcastName}
                    onChange={(e) => setPodcastName(e.target.value)}
                    placeholder="Podcast Name"
                    className='border-2 rounded-2xl p-2 text-black m-8'
                    required
                />
                <input
                    type="text"
                    value={episodeName}
                    onChange={(e) => setEpisodeName(e.target.value)}
                    placeholder="Episode Name"
                    className='border-2 rounded-2xl p-2 text-black m-8'
                    required
                />
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"  type="submit" disabled={isLoading}>
                    {isLoading ? 'Loading...' : 'Lets Summarize!'}
                </button>
            </form>
            {summary && (
                <div className="my-8 lg:w-2/3 w-4/5 overflow-auto border-2 rounded-2xl lg:p-10 p-4 lg:text-md text-xs">
                    <pre className="whitespace-pre-wrap">{summary}</pre>
                </div>
            )}
        </div>
    );
}