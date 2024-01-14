const baseURL = 'http://localhost:8000/api';


export async function postFastAPIText(
    endpoint: string,
    podcastName: string, 
    episodeName: string,
    clientId: string
): Promise<Response> {
    const url = `${baseURL}/${endpoint}/`;
    const jsonData = {
        podcast_name: podcastName, 
        episode_name: episodeName, 
        client_id: clientId
    };
    const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(jsonData),
        headers: {
            'Content-Type': 'application/json',
        },
    });
    return response;
}