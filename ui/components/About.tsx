"use client";
import Link from "next/link";

export default function About(){
    return(
        <section className="flex justify-center items-center w-full h-screen bg-gray-100 dark:bg-gray-800">
            <div className="text-center">
                <h1 className="text-2xl font-bold tracking-tighter sm:text-2xl md:text-4xl lg:text-5xl text-gray-900 dark:text-gray-100">
                    About
                </h1>
                <div className="max-w-xl mx-auto">
                    <p className="mt-4 text-gray-500 md:text-xl dark:text-gray-400">
                        This app facilitates podcast episode summaries by leveraging the Google Gemini API for transcription summarization. 
                        Contributions to the project are encouraged. For additional details, please visit  
                        <Link href="https://github.com/PooriaT/Sumcast" target="_blank" className="text-blue-500">Github</Link>.
                        Feel free to reach out via email at <Link href="mailto:pooria@duck.com" target="_blank" className="text-blue-500">pooria@duck.com</Link> 
                        or visit my personal page at <Link href="https://pooriat.com" target="_blank" className="text-blue-500">pooriat.com</Link>.
                        If you would like to support the project, consider <Link href="https://www.buymeacoffee.com/pooria7" target="_blank" className="text-blue-500">buying me a book</Link>.
                        Your support is appreciated.
                    </p>
                </div>
            </div>
        </section>
    )
}