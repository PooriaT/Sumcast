"use client";

export default function About(){
    return(
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-gray-100 dark:bg-gray-800">
        <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
            <div className="space-y-2">
                <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl lg:text-7xl text-gray-900 dark:text-gray-100">
                About Our Service
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl dark:text-gray-400">
                We provide top-notch services that will boost your productivity. Join us and experience the difference.
                </p>
            </div>
            </div>
        </div>
        </section>
    )
}