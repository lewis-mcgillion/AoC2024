package main

import (
	"fmt"
	"os"
	"log"
	"strconv"
	"bufio"
	"strings"
	"sort"
	"math"
)

func main() {
    file, err := os.Open("01_input.txt")
	if err != nil{
		log.Fatalf("failed to open file")
	}
	defer file.Close()

	var column1, column2 []float64
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		if len(line) < 2 {
			log.Fatalf("Invalid line in file: %s", scanner.Text())
		}
		val1, err := strconv.ParseFloat(line[0], 64)
		if err != nil {
			log.Fatalf("Failed to parse number: %v", err)
		}
		val2, err := strconv.ParseFloat(line[1], 64)
		if err != nil {
			log.Fatalf("Failed to parse number: %v", err)
		}
		column1 = append(column1, val1)
		column2 = append(column2, val2)
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	sort.Float64s(column1)
	sort.Float64s(column2)
	
	if len(column1) != len(column2) {
		fmt.Println("Error: Slices must have the same length")
		return
	}

	differenceAbsolute := make([]float64, len(column1))
	for i := range column1 {
		differenceAbsolute[i] = math.Abs(column1[i] - column2[i])
	}

	var totalDifference = 0.0

	for i := range differenceAbsolute {
		totalDifference += differenceAbsolute[i]
	}
	fmt.Printf("Total difference between columns: %d\n", int(totalDifference))

	//pt2 similarity score
	//hash map of how many times values exist in col2, check each col1 value against it
	countMap := make(map[float64]int)
	for _, val := range column2 {
		countMap[val]++
	}

	globalSimilarity := 0
	for _, val := range column1 {
		if count, exists := countMap[val]; exists {
			globalSimilarity += count * int(val)
		}
	}
	fmt.Printf("Global similarity: %d\n", globalSimilarity)
}