"use client";
import Image from "next/image";

export default function Hero() {
    return (
        <section className="flex justify-center items-center w-full h-screen bg-gray-100 dark:bg-gray-800">
            <div className="text-center grid grid-cols-2">
                <div>
                    <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl lg:text-7xl text-gray-900 dark:text-gray-100">
                        Welcome to Sumcast!
                    </h1>
                    <p className="mt-4 text-gray-500 md:text-xl dark:text-gray-400">
                        You can summarize your podcast episodes in just a few clicks.
                    </p>
                    <a href="#main">
                        <button className="btn mt-8 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                            Summarizing!
                        </button>
                    </a>
                </div>
                <div className="flex">
                    <Image 
                        src="/hero.svg" 
                        alt="Hero Component Image" 
                        width="0"
                        height="0"
                        sizes="100vw"
                        className="w-full h-auto"
                    />
                </div>
            </div>
        </section>
    );
}

