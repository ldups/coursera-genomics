states = new Array(8);
for (let i=0;i<8;i++){
    states[i] = new Array(8)
}

mineLocations = new Array(10);
for (let i=0;i<10;i++){
    mineLocations[i]= Math.floor(Math.random()*64)
}


mines = new Array(8);
for (let i=0;i<8;i++){
    mines[i] = new Array(8)
}
for (let i=0;i<8;i++){
    for (let j=0;j<8;j++){
        if(mineLocations.includes(i*8 + j)){
            mines[i][j]= true;
        }
        else{
            mines[i][j] = false;
        }
    }
}

print(states)
print(mines)
print(mineLocations)



