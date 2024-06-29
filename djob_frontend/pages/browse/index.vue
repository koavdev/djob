<script setup>


// Categories

const { data: jobCategories } = await useFetch('http://localhost:8000/api/v1/jobs/categories/')

let selectedCategoriesRef = ref('')
let selectedCategories = []

function toggleCategory(id) {
    const index = selectedCategories.indexOf(id)

    if (index === -1) {
        selectedCategories.push(id)
    } else {
        selectedCategories.splice(index, 1)
    }

    console.log('toggleCategory', selectedCategories.join(','))

    selectedCategoriesRef.value = selectedCategories.join(',')
}

//

let {data: jobs} = await useFetch('http://localhost:8000/api/v1/jobs/', {
    query: {
        categories: selectedCategoriesRef
    }
})


</script>

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
                 <p 
                    v-for="category in jobCategories"
                    v-bind:key="category.id"
                    v-on:click="$event => toggleCategory(category.id)"
                    v-bind:class="{'bg-teal-900': selectedCategoriesRef.includes(category.id)}"
                    class="py-4 px-6 text-white rounded-xl"
                >
                    {{ category.title }}
                </p> 

            </div>
        </div>

        <div class="md:col-span-3">
            <div class="space-y-4">
                <Job 
                    v-for="job in jobs"
                    v-bind:key="job.id"
                    v-bind:job="job"/>
            </div>
        </div>
    </div>
</template>