import StatusCard from '@/components/StatusCard.vue'

export default {
  title: 'Components/StatusCard',
  component: StatusCard,
  tags: ['autodocs'],
  argTypes: {
    status: {
      control: { type: 'select' },
      options: ['enqueued', 'finished', 'failed', 'scheduled', 'started']
    }
  }
}

export const Default = {
  args: {
    status: 'enqueued'
  }
}
