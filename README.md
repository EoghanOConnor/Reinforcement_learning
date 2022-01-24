# Reinforcement_learning with q-table

This is a proof of concept that a reinforcement agent can determine which training intensities are best suited for an athlete to improve the times of a given distance.
In this example, 2k times are created to represent an athlete. This athlete improves the most when the aerobic thershold makes up approx 70%-80% of the athletes training program.
From this we can see that the agent discovers through exploration and the use of a q-table that the best training strategy is to keep the athlete between these 2 intensities.
#Below is the athletes times vs the percentage of their training they spend in aerobic thershold
![image](https://user-images.githubusercontent.com/45408401/150753061-5fa61f0a-e1ee-4e31-8f55-0e7f6acc4828.png)

#Below is the agent exploring the different 3 different intensities. It determines the best ratio after numerous iterations.
![image](https://user-images.githubusercontent.com/45408401/150754158-33e2989a-db56-400a-955e-be7d89d4794a.png)

This developed in python and in jupyter notebook. To run you will need to install these.
