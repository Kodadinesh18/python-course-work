#program for photo_gallery:


photo_gallery=["beach.png","mountain.png","party1.png","selfie.png","birthday.png","concert.png","sunset.png","trip1.png"]

for i in range(0,len(photo_gallery)):
    print(f"{i+1}.{photo_gallery[i]}")

selected_pics=set(map(int,input("select photos to share(enter numbers separated by commas):").split(",")))
print(selected_pics)
print("the photos selected:")
for index in selected_pics:
    print(photo_gallery[index-1])
