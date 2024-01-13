"use client";

import React, { useState } from 'react';


export default function Main() {
    const [podcastName, setPodcastName] = useState('');
    const [episodeName, setEpisodeName] = useState('');
    const [summary, setSummary] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        if (!podcastName.trim() || !episodeName.trim()) {
            alert('Both fields are required.');
            return;
        }

        setIsLoading(true);
        setSummary('');
        try {
            const response = await fetch('http://localhost:8000/api/summarize/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ podcast_name: podcastName, episode_name: episodeName }),
            });

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
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={podcastName}
                    onChange={(e) => setPodcastName(e.target.value)}
                    placeholder="Podcast Name"
                    required
                />
                <input
                    type="text"
                    value={episodeName}
                    onChange={(e) => setEpisodeName(e.target.value)}
                    placeholder="Episode Name"
                    required
                />
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"  type="submit" disabled={isLoading}>
                    {isLoading ? 'Loading...' : 'Submit'}
                </button>
            </form>
            {summary && (
                <div className="lg:w-2/3 w-4/5 overflow-auto border-2 rounded-2xl lg:p-10 p-4 lg:text-md text-xs">
                    <pre className="whitespace-pre-wrap">{summary}</pre>
                </div>
            )}
        </div>
    );
}