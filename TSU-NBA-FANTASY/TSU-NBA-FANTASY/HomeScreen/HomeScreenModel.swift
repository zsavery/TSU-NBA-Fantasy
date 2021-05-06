//
//  HomeScreenModel.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 3/15/21.
//

import Foundation

protocol HomesScreenModelDelegateProtocol {
    func dataFetched()
}

class HomeScreenModel {
    private let jsonUrlString = "https://tsufansite.com/info.php"
    var delegate: HomesScreenModelDelegateProtocol
    var playerData = [Player]()
    
    init(delegate: HomesScreenModelDelegateProtocol) {
        self.delegate = delegate
        fetchData()
    }
    
    private func fetchData() {
        guard let url =  URL(string: jsonUrlString) else {return}
        
        URLSession.shared.dataTask(with: url){(data, responce, err) in
            guard let data = data else {return}
            let dataAsString = String(data: data, encoding: .utf8)
            //print(dataAsString)
            
            do{
                let json = try JSONSerialization.jsonObject(with: data, options: [.mutableContainers, .allowFragments])
                print(json)
                
            } catch let jsonErr{
                
                print("error serializing json: ", jsonErr)
            }
            
            var newtxt: String? = dataAsString
            
            let wordsToRemove = ["Playerid: ", "First Name: ", "Last Name: ", "TeamID: ", "Pos: ", "Points: ", "Rebounds: ", "Assists: ", "Steals: " , "Blocks: ", "TurnOvers: ", "Fantasy ", " Jr.", " III", " II", " IV", " Sr."]
            for wordToRemove in wordsToRemove{
                while newtxt!.contains(wordToRemove) {
                    if let range2 = newtxt!.range(of: wordToRemove) {
                        newtxt!.removeSubrange(range2)
                    }
                }
            }
            
            newtxt = newtxt!.replacingOccurrences(of: " ", with: ", ")
            newtxt = newtxt!.replacingOccurrences(of: "<br>", with: "\n")
            newtxt = newtxt!.replacingOccurrences(of: "\n", with: ", ")
            //print("Swap spaces with commas: \n\(newtxt!)")
            
            var txtArr: [String] = newtxt!.components(separatedBy: ", ")
            
            //for val in txtArr{
            //print(val)
            //}
            //var myNewDictArray: [[String:Any]]
            //var tempDict: [String: Any]
            
            //print("Count txtArr: \n\(txtArr.count)")
            
            var index = 0
            let keyNum = 12
            
            var stat = Player()
            var PlayerStats = [Player()]
            txtArr.removeLast()
            for value in txtArr{
                if(index > (keyNum-1)){
                    index = 0
                }
                let val: String? = value
                switch index {
                case 0:
                    stat.PlayerId = val ?? "NA"
                    print("PlayerId: " + stat.PlayerId)
                case 1:
                    stat.FirstName = val ?? "NA"
                    print("First Name: " + stat.FirstName)
                case 2:
                    stat.LastName = val ?? "NA"
                    print("Last Name: " + stat.LastName)
                case 3:
                    stat.TeamId = val ?? "NA"
                    print("TeamId: " + stat.TeamId)
                case 4:
                    stat.Pos = val ?? "NA"
                    print("Position: " + stat.Pos)
                    
                case 5:
                    stat.Points = round(Float(val ?? "0") ?? 0)
                    print("Points: \(stat.Points)")
                case 6:
                    stat.Rebounds = round(Float(val ?? "0") ?? 0)
                    print("Rebounds: \(stat.Rebounds)")
                case 7:
                    stat.Assists = round(Float(val ?? "0") ?? 0)
                    print("Assists: \(stat.Assists)")
                case 8:
                    stat.Steals = round(Float(val ?? "0") ?? 0)
                    print("Steals: \(stat.Steals)")
                case 9:
                    stat.Blocks = round(Float(val ?? "0") ?? 0)
                    print("Blocks: \(stat.Blocks)")
                case 10:
                    stat.Turnovers = round(Float(val ?? "0") ?? 0)
                    print("Turnovers: \(stat.Turnovers)")
                case 11:
                    stat.FantasyPoints = round(Float(val ?? "0") ?? 0)
                    PlayerStats.append(stat)
                    print("Fantasy Points: \(stat.FantasyPoints)")
                default:
                    print("Something went wrong!")
                }
                //print(stat)
                index+=1
                
            }
            PlayerStats.removeFirst()
            self.playerData = PlayerStats
            self.delegate.dataFetched()
            
        }.resume()
    }
}

struct Player {
    var PlayerId: String = "NA"
    var FirstName: String = "NA"
    var LastName: String = "NA"
    var Pos: String = "NA"
    var TeamId: String = "NA"
    var Points: Float = 0
    var Rebounds: Float = 0
    var Assists: Float = 0
    var Steals: Float = 0
    var Blocks: Float = 0
    var Turnovers: Float = 0
    var FantasyPoints: Float = 0
    var name:String {
        return "\(FirstName)  \(LastName)"
    }
}
