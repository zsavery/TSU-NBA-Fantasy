//
//  main.swift
//  TestingParseWebsite
//
//  Created by Zyon Savery on 5/2/21.
//

import Foundation
var hugetxt = """
Playerid: 2 First Name: Quincy Last Name: Acy TeamID: 28 Pos: NA Points: 2.8 Rebounds: 1.8 Assists: 1.2 Steals: 3 Blocks: 0.8 TurnOvers: 0.4 Fantasy Points: 8.36
Playerid: 4 First Name: Steven Last Name: Adams TeamID: 23 Pos: C Points: 9.0 Rebounds: 10.0 Assists: 2.2 Steals: Blocks: 0.8 TurnOvers: 0.4 Fantasy Points: 25.900000000000002
Playerid: 12 First Name: Al-Farouq Last Name: Aminu TeamID: 6 Pos: Points: 0.0 Rebounds: 0.6 Assists: 0.2 Steals: Blocks: 0.0 TurnOvers: 0.0 Fantasy Points: 1.02
Playerid: 18 First Name: Kyle Last Name: Anderson TeamID: 19 Pos: PF Points: 10.2 Rebounds: 7.2 Assists: 4.6 Steals: Blocks: 1.4 TurnOvers: 0.4 Fantasy Points: 30.14
Playerid: 20 First Name: Giannis Last Name: Antetokounmpo TeamID: 21 Pos: PF Points: 25.4 Rebounds: 10.8 Assists: 5.0 Steals: Blocks: 0.6 TurnOvers: 3.0 Fantasy Points: 47.260000000000005
Playerid: 21 First Name: Carmelo Last Name: Anthony TeamID: 29 Pos: Points: 16.0 Rebounds: 3.2 Assists: 1.6 Steals: Blocks: 0.2 TurnOvers: 1.0 Fantasy Points: 22.44
Playerid: 23 First Name: Trevor Last Name: Ariza TeamID: 20 Pos: PF Points: 11.6 Rebounds: 7.0 Assists: 2.4 Steals: Blocks: 0.4 TurnOvers: 1.0 Fantasy Points: 24.6
Playerid: 28 First Name: D.J. Last Name: Augustin TeamID: 14 Pos: Points: 8.333333333333334 Rebounds: 1.0 Assists: 4.0 Steals: Blocks: 0.0 TurnOvers: 1.0 Fantasy Points: 15.2
Playerid: 33 First Name: Wade Last Name: Baldwin IV TeamID: 29 Pos: Points: 0.8 Rebounds: 1.2 Assists: 0.4 Steals: Blocks: 0.0 TurnOvers: 0.6 Fantasy Points: 2.64
Playerid: 35 First Name: J.J. Last Name: Barea TeamID: 8 Pos: Points: 0.6 Rebounds: 0.0 Assists: 0.0 Steals: Blocks: 0.0 TurnOvers: 0.2 Fantasy Points: 0.39999999999999997
Playerid: 36 First Name: Harrison Last Name: Barnes TeamID: 30 Pos: SF Points: 19.6 Rebounds: 5.6 Assists: 3.6 Steals: Blocks: 0.0 TurnOvers: 2.6 Fantasy Points: 29.919999999999995
Playerid: 38 First Name: Will Last Name: Barton TeamID: 9 Pos: SG Points: 13.8 Rebounds: 3.0 Assists: 3.6 Steals: Blocks: 0.2 TurnOvers: 2.4 Fantasy Points: 22.4
Playerid: 40 First Name: Nicolas Last Name: Batum TeamID: 16 Pos: Points: 7.4 Rebounds: 4.2 Assists: 1.8 Steals: Blocks: 1.6 TurnOvers: 1.4 Fantasy Points: 18.540000000000003
Playerid: 42 First Name: Aron Last Name: Baynes TeamID: 38 Pos: Points: 0.0 Rebounds: 0.0 Assists: 0.0 Steals: Blocks: 0.0 TurnOvers: 0.0 Fantasy Points: 0.0
Playerid: 44 First Name: Kent Last Name: Bazemore TeamID: 11 Pos: SG Points: 10.4 Rebounds: 3.0 Assists: 1.4 Steals: Blocks: 0.0 TurnOvers: 2.0 Fantasy Points: 15.700000000000003
"""

var newtxt = hugetxt

let wordsToRemove = ["Playerid: ", "First Name: ", "Last Name: ", "TeamID: ", "Pos: ", "Points: ", "Rebounds: ", "Assists: ", "Steals: " , "Blocks: ", "TurnOvers: ", "Fantasy "]
for wordToRemove in wordsToRemove{
    while newtxt.contains(wordToRemove) {
        if let range2 = newtxt.range(of: wordToRemove) {
            newtxt.removeSubrange(range2)
        }
    }
}

newtxt = newtxt.replacingOccurrences(of: " ", with: ", ")
//print("Swap spaces with commas: \n\(newtxt)")

//var txtArr = newtxt.components(separatedBy: ", ")
var txtArr = newtxt.components(separatedBy: CharacterSet(charactersIn: "\n"))
var txtNestedArr: [[String]] = []

for item in txtArr{
    let tempArr = item.components(separatedBy:  ",")
    txtNestedArr.append(tempArr)
}

var myNewDictArray: [[String:Any]]
var tempDict: [String: Any]

print("Count txtArr: \n\(txtArr.count)")

var index = 0
var keyNum = 12

struct PlayerStat {
    var PlayerId: String?
    var FirstName: String?
    var LastName: String?
    var TeamId: String?
    var Pos: String?
    var Points: Double = 0
    var Rebounds: Double = 0
    var Assists : Double = 0
    var Steals: Double = 0
    var Blocks: Double = 0
    var TurnOvers: Double = 0
    var FantasyPoints: Double = 0
}

var stat = PlayerStat()
var PlayerStats = [PlayerStat]()

for arr in txtNestedArr{
    for value in arr{
        if(index > (keyNum-1)){
            index = 0
        }
        print(value)
        
        
        switch index {
            case 0:
                stat.PlayerId = value
                print("PlayerId: " + stat.PlayerId!)
            case 1:
                stat.FirstName = value
                print("First Name: " + stat.FirstName!)
            case 2:
                stat.LastName = value
                print("Last Name: " + stat.LastName!)
            case 3:
                stat.TeamId = value
                print("TeamId: " + stat.TeamId!)
            case 4:
                stat.Pos = value
                print("Position: " + stat.Pos!)
            case 5:
                stat.Points = round(Double(value) ?? 0)
                print("Points: \(stat.Points)")
            case 6:
                stat.Rebounds = round(Double(value) ?? 0)
                print("Rebounds: \(stat.Rebounds)")
            case 7:
                stat.Assists = round(Double(value) ?? 0)
                print("Assists: \(stat.Assists)")
            case 8:
                stat.Steals = round(Double(value) ?? 0)
                print("Steals: \(stat.Steals)")
            case 9:
                stat.Blocks = round(Double(value) ?? 0)
                print("Blocks: \(stat.Blocks)")
            case 10:
                stat.TurnOvers = round(Double(value) ?? 0)
                print("TurnOvers: \(stat.TurnOvers)")
            case 11:
                stat.FantasyPoints = round(Double(value) ?? 0)
                print("FantasyPoints: \(stat.FantasyPoints)")
            default:
                print("Something went wrong!")
        }
        index+=1
         
    }
 
    
    

}
print(stat)




