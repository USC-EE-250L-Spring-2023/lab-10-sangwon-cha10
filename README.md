# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
Done individually

## Lab Question Answers

# Question 1: Under what circumstances do you think it will be worthwhile to offload one or both of the processing tasks to your PC? And conversely, under what circumstances will it not beworthwhile?
It would be worthwhile when the PC is not performing other tasks in parallel so that it would be still faster than performing either on Raspberry Pi. If PC is busy taking care of other tasks at the time
when the tasks are offloaded, it may be slower.

# Question 2: Why do we need to join the thread here?
Because the main thread, which is invoking join(), needs to wait for the referenced thread to complete its task. This prevents the main thread terminating before the requested task is finished.

# Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?
        #   See this article: https://oxylabs.io/blog/concurrency-vs-parallelism
        #   ChatGPT is also good at explaining the difference between parallel and concurrent execution!
        #   Make sure to cite any sources you use to answer this question.
They are running parallel as the process is using different cores on different processors. As some tasks are offloaded to PC, some tasks are being taken care of by Raspberry Pi's processor
in parallel with the tasks that the PC is carrying out. Concurrency refers to the processor switching back and forth between multiple tasks.

# Question 4: What is the best offloading mode? Why do you think that is?
Both is the best offloading mode. I think it's because PC has a faster processor, so it can perform tasks much faster than Raspberry Pi can.

# Question 5: What is the worst offloading mode? Why do you think that is?
None is the worst. The Raspberry Pi's processor is much slower.
 
# Question 6: The processing functions in the example aren't very likely to be used in a real-world application. 
    #   What kind of processing functions would be more likely to be used in a real-world application?
    #   When would you want to offload these functions to a server?
Processing for machine learning algorithms would be better dealt in cloud servers.