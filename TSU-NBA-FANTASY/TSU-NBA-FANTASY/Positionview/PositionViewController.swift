//
//  PositionviewController.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit

class PositionViewController: UIViewController {
    var positionView: PositionView!
    var positionViewModel: PositionViewModel!
    
    init(frame: CGRect) {
        super.init(nibName: nil, bundle: nil)
        self.positionView = PositionView(frame: frame)
        self.positionViewModel = PositionViewModel(delegate: self)
        self.view = self.positionView
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func setPlayer(player:Player) {
        self.positionViewModel.player = player
    }
}

extension PositionViewController: PositionViewModelDelegate {
    func newPlayerSet() {
        positionView.scoreLabel.text = String(describing: positionViewModel.player.FantasyPoints)
        positionView.ptsLabel.text = String(describing: positionViewModel.player.Points)
        positionView.blkLabel.text =  String(describing: positionViewModel.player.Blocks)
        positionView.scoreLabel.text = String(describing: positionViewModel.player.FantasyPoints)
        positionView.astLabel.text =  String(describing: positionViewModel.player.Assists)
        positionView.stlLabel.text =  String(describing: positionViewModel.player.Steals)
        positionView.toLabel.text =  String(describing: positionViewModel.player.Turnovers)
    }
}
