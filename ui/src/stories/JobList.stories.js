import JobList from '@/components/JobList.vue'

export default {
  title: 'Components/JobList',
  component: JobList,
  tags: ['autodocs']
}

export const Default = {
  args: {
    jobs: [
      {
        job_id: '444927b6-6c1a-40b1-b006-9addf93eb0ab',
        job_status: 'failed'
      },
      {
        job_id: '255eeabb-d3e5-4d8b-a8da-b8164737d00c',
        job_status: 'finished'
      },
      {
        job_id: '37ac515d-cdad-413a-a165-355db7d8f776',
        job_status: 'scheduled'
      }
    ]
  }
}
