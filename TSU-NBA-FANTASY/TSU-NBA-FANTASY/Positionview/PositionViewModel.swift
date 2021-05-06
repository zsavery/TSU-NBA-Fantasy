//
//  PositionviewModel.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
protocol PositionViewModelDelegate {
    func newPlayerSet()
}
class PositionViewModel {
    var delegate: PositionViewModelDelegate
    var player:Player! {
        didSet {
            self.delegate.newPlayerSet()
        }
    }
    
    init(delegate: PositionViewModelDelegate) {
        self.delegate = delegate
    }
}
