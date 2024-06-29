<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '~/stores/user'

const userStore = useUserStore()
const router = useRouter()
let jobs = ref()

onMounted(() => {
  if (!userStore.user.isAuthenticated) {
    router.push('/login')
  } else {
    getJobs()
  }
})

useSeoMeta({
    title: 'My jobs',
    ogTitle: 'My jobs',
    description: 'The description'
})

async function getJobs() {
    $fetch('http://localhost:8000/api/v1/jobs/my', {
        headers: {
            'Authorization': 'token ' + userStore.user.token,
            'Content-Type': 'application/json'
        },
    }).then(response => {
        jobs.value = response
    }).catch( error => {
        console.log('error', error)
    })
}

</script>

<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">My jobs</h1>

        <div class="space-y-4">
                <Job 
                    v-for="job in jobs"
                    v-bind:key="job.id"
                    :job="job"
                    :my=true
                    />
            </div>
    </div>
</template>