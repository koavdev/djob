<template>
    <div class="grid md:grid-cols-4 gap-3 py-10 px-6">
        <div class="md:col-span-1 px-6 py-6 bg-teal-700 rounded-xl">
            <div class="flex space-x-4">
                <input type="search" placeholder="Find a job..." class="w-full px-6 py-4 rounded-xl" />

                <button class="px-6 py-4 bg-teal-900 text-white rounded-xl">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                    </svg>

                </button>
            </div>

            <hr class="my-6 opacity-6"></hr>

            <h3 class="mt-6 text-xl text-white">Categories</h3>

            <div class="mt-6 space-y-4">
                 <p class="py-4 px-6 text-white rounded-xl">Category 1</p> 
                 <p class="py-4 px-6 text-white rounded-xl">Category 2</p> 
                 <p class="py-4 px-6 text-white rounded-xl">Category 3 </p> 
            </div>
        </div>

        <div class="md:col-span-3">
            <div class="space-y-4">
                <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
                    <div>
                        <h3 class="mb-2 text-xl font-semibold">The job position</h3>
                        <p class="text-gray-600">The company name</p>
                    </div>

                    <div>
                        <p class="mb-2">Worldwide</p>
                        <p>$90-120k</p>
                    </div>

                    <div>
                        <p>Posted Dec. 1 2022</p>
                    </div>

                    <div>
                        <NuxtLink to="/browse/1" class="py-4 px-6 bg-teal-700 text-white rounded-xl">Details</NuxtLink>
                    </div>
                </div>
                <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
                    <div>
                        <h3 class="mb-2 text-xl font-semibold">The job position</h3>
                        <p class="text-gray-600">The company name</p>
                    </div>

                    <div>
                        <p class="mb-2">Worldwide</p>
                        <p>$90-120k</p>
                    </div>

                    <div>
                        <p>Posted Dec. 1 2022</p>
                    </div>

                    <div>
                        <NuxtLink to="/browse/1" class="py-4 px-6 bg-teal-700 text-white rounded-xl">Details</NuxtLink>
                    </div>
                </div>
                <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
                    <div>
                        <h3 class="mb-2 text-xl font-semibold">The job position</h3>
                        <p class="text-gray-600">The company name</p>
                    </div>

                    <div>
                        <p class="mb-2">Worldwide</p>
                        <p>$90-120k</p>
                    </div>

                    <div>
                        <p>Posted Dec. 1 2022</p>
                    </div>

                    <div>
                        <NuxtLink to="/browse/1" class="py-4 px-6 bg-teal-700 text-white rounded-xl">Details</NuxtLink>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>