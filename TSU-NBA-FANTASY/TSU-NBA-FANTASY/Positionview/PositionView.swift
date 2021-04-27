//
//  Positionview.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit

protocol PositionViewDelegate {
    
}

class PositionView: UIView {
    
    init(frame: CGRect, delegate: PositionViewDelegate) {
        super.init(frame: frame)
        self.backgroundColor = UIColor.blue
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
