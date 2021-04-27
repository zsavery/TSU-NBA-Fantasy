//
//  OutterView.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit

protocol OutterViewDelegate {
    func menuButtonTapped()
    func menuOptionSelected(option: String)
}

class OutterView: UIView {
    final let LeftSpacing: CGFloat = 20.0
    final let TopButtonSpacing: CGFloat = 35.0
    final let OptionsMenuWidth: CGFloat = 100.0
    
    let contentView: UIView
    let menuButton: UIButton
    let titleLabel: UILabel
    let searchBar: UISearchBar
    var menuOptionsStackView: UIStackView!
    let delegate: OutterViewDelegate
    
    
    init(frame: CGRect, delegate: OutterViewDelegate, menuOptions: [String]) {
        self.contentView = UIView()
        self.menuButton = UIButton()
        self.titleLabel = UILabel()
        self.searchBar = UISearchBar()
        self.delegate = delegate
        super.init(frame: frame)
        
        setupView(menuOptions: menuOptions)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func setupView(menuOptions: [String]) {
        self.backgroundColor = UIColor.orange
       
        self.contentView.frame = CGRect(x: LeftSpacing, y: 75, width: self.bounds.width - LeftSpacing * 2, height: self.bounds.height - 100)
        self.contentView.backgroundColor = UIColor.white
        self.addSubview(contentView)

        self.menuButton.frame = CGRect(x: LeftSpacing, y: TopButtonSpacing, width: 30, height: 30)
        self.menuButton.backgroundColor = .black
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(menuButtonTapped))
        self.menuButton.addGestureRecognizer(tapGesture)
        self.addSubview(menuButton)
        
        self.titleLabel.frame = CGRect(x: 70, y: 35, width: self.bounds.width - 140, height: 30)
        self.titleLabel.backgroundColor = .black
        self.titleLabel.textColor = .orange
        self.titleLabel.text = "Some title"
        self.titleLabel.textAlignment = .center
        self.addSubview(titleLabel)
        
        setupMenu(menuOptions: menuOptions)
    }
    
    //MARK: Actions
    @objc func menuButtonTapped() {
        self.delegate.menuButtonTapped()
        
    }
    
    @objc func menuOptionSelected(sender: UITapGestureRecognizer) {
        guard let label = sender.view as? UILabel,
        let option = label.text else {
            return
        }
        self.delegate.menuOptionSelected(option: option)
    }
    
    //MARK: Public
    func showMenuOptions() {
        self.menuOptionsStackView.isHidden = false
    }
    
    func hideMenuOptions()  {
        self.menuOptionsStackView.isHidden = true
    }
    
    func showView(view: UIView, title: String) {
        self.contentView.subviews.first?.removeFromSuperview()
        self.contentView.addSubview(view)
        self.titleLabel.text = title
    }
    
    //MARK: Private
    func setupMenu(menuOptions: [String]) {
        var optionLabelArray = [UILabel]()
        for (n, option) in menuOptions.enumerated() {
            let label = UILabel()
            label.text = option
            label.textAlignment = .center
            label.textColor = .white
            label.layer.borderColor = UIColor.green.cgColor
            label.layer.borderWidth = 1
            label.backgroundColor = .black
            let tapGesture = UITapGestureRecognizer(target: self, action: #selector(menuOptionSelected(sender:)))
            label.addGestureRecognizer(tapGesture)
            label.isUserInteractionEnabled = true
            label.widthAnchor.constraint(equalToConstant: OptionsMenuWidth).isActive = true
            optionLabelArray.insert(label, at: n)
        }
        
        self.menuOptionsStackView = UIStackView(arrangedSubviews: optionLabelArray)
        self.menuOptionsStackView.axis = .vertical
        self.menuOptionsStackView.alignment = .center
        self.menuOptionsStackView.distribution = .fillEqually
        self.menuOptionsStackView.backgroundColor = .black
        self.menuOptionsStackView.frame = CGRect(x: LeftSpacing, y: TopButtonSpacing, width: OptionsMenuWidth, height: 100)
        self.addSubview(self.menuOptionsStackView)
        self.menuOptionsStackView.isHidden = true
    }    
}

